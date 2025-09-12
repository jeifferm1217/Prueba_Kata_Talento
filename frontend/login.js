const API_URL = "http://127.0.0.1:8000"; // tu backend FastAPI

const form = document.getElementById("form");
const usernameInput = document.getElementById("username-input"); // cambiar id en el HTML a username-input
const passwordInput = document.getElementById("password-input");
const errorMessage = document.getElementById("error-message");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const username = usernameInput.value.trim();
  const password = passwordInput.value.trim();

  if (!username || !password) {
    errorMessage.textContent = "Por favor llena todos los campos";
    return;
  }

  try {
    // Enviar login como x-www-form-urlencoded
    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", password);

    const res = await fetch(`${API_URL}/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: formData
    });

    const data = await res.json();

    if (res.ok) {
      localStorage.setItem("token", data.access_token);
      window.location.href = "notas.html";
    } else {
      errorMessage.textContent = data.detail || "Nombre de usuario o contraseña incorrectos";
    }
  } catch (err) {
    errorMessage.textContent = "Error de conexión con el servidor";
    console.error(err);
  }
});
