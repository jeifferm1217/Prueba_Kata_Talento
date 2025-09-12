const API_URL = "http://127.0.0.1:8000"; // tu backend FastAPI

// --- LOGOUT ---
function logout() {
  localStorage.removeItem("token");
  window.location.href = "login.html";
}

// --- OBTENER NOTAS ---
async function obtenerNotas() {
  const token = localStorage.getItem("token");
  if (!token) return window.location.href = "login.html";

  const res = await fetch(`${API_URL}/notas/`, {
    headers: { Authorization: `Bearer ${token}` }
  });

  const notas = await res.json();
  const lista = document.getElementById("listaNotas");
  lista.innerHTML = "";

  notas.forEach(nota => {
    const div = document.createElement("div");
    div.innerHTML = `
      <h3>${nota.titulo}</h3>
      <div>${marked.parse(nota.contenido_markdown)}</div>
      <button onclick="editarNota(${nota.id}, '${nota.titulo}', \`${nota.contenido_markdown}\`)">Editar</button>
      <button onclick="eliminarNota(${nota.id})">Eliminar</button>
    `;
    lista.appendChild(div);
  });
}

// --- GUARDAR NOTA ---
async function guardarNota(id = null) {
  const token = localStorage.getItem("token");
  const titulo = document.getElementById("tituloNota").value;
  const contenido = document.getElementById("contenidoNota").value;

  const method = id ? "PUT" : "POST";
  const url = id ? `${API_URL}/notas/${id}` : `${API_URL}/notas/`;

  await fetch(url, {
    method,
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify({ titulo, contenido_markdown: contenido })
  });

  document.getElementById("tituloNota").value = "";
  document.getElementById("contenidoNota").value = "";
  obtenerNotas();
}

// --- EDITAR NOTA ---
function editarNota(id, titulo, contenido) {
  document.getElementById("tituloNota").value = titulo;
  document.getElementById("contenidoNota").value = contenido;
  document.querySelector("button[onclick='guardarNota()']").onclick = () => guardarNota(id);
}

// --- ELIMINAR NOTA ---
async function eliminarNota(id) {
  const token = localStorage.getItem("token");
  await fetch(`${API_URL}/notas/${id}`, {
    method: "DELETE",
    headers: { Authorization: `Bearer ${token}` }
  });
  obtenerNotas();
}

// --- CARGAR NOTAS AL INICIAR ---
if (window.location.pathname.includes("notas.html")) obtenerNotas();
