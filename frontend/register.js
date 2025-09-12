const API_URL = "http://127.0.0.1:8000"; // tu backend FastAPI

const form = document.getElementById("form");
const nombreInput = document.getElementById("firstname-input");
const emailInput = document.getElementById("email-input");
const passwordInput = document.getElementById("password-input");
const repeatPasswordInput = document.getElementById("repeat-password-input");
const errorMessage = document.getElementById("error-message");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const nombre = nombreInput.value.trim();
  const email = emailInput.value.trim();
  const password = passwordInput.value.trim();
  const repeatPassword = repeatPasswordInput.value.trim();

  if (!nombre || !email || !password || !repeatPassword) {
    errorMessage.textContent = "Por favor completa todos los campos";
    return;
  }

  if (password !== repeatPassword) {
    errorMessage.textContent = "Las contraseñas no coinciden";
    return;
  }

  try {
    const res = await fetch(`${API_URL}/usuarios/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        nombre_usuario: nombre,
        correo: email,
        contraseña: password
      })
    });

    const data = await res.json();

    if (res.ok) {
      alert("Registro exitoso. Ahora inicia sesión");
      window.location.href = "login.html";
    } else {
      errorMessage.textContent = data.detail || "Error al registrar usuario";
    }
  } catch (err) {
    errorMessage.textContent = "Error de conexión con el servidor";
    console.error(err);
  }
});
