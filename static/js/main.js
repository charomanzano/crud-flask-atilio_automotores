// Obtener referencia al enlace "Ingresos" del navbar
const linkIngresos = document.getElementById("ingresos-link");

// Obtener referencia al contenedor de ingresos
const ingresosContainer = document.getElementById("ingresos-container");

// Obtener referencia al contenedor de resultados
const resultadosContainer = document.getElementById("resultados-table");

// Ocultar el contenedor de ingresos y resultados inicialmente
ingresosContainer.style.display = "none";
resultadosContainer.style.display = "none";

// Agregar evento click al enlace "Ingresos"
linkIngresos.addEventListener("click", function () {
  // Mostrar el contenedor de ingresos y resultados
  ingresosContainer.style.display = "block";
  resultadosContainer.style.display = "block";

  // Actualizar la URL para incluir el fragmento "ingresos-container"
  window.location.hash = "ingresos-container";
});

// Verificar si el hash en la URL coincide con el ID del contenedor de ingresos
if (window.location.hash === "#ingresos-container") {
  // Mostrar el contenedor de ingresos y resultados
  ingresosContainer.style.display = "block";
  resultadosContainer.style.display = "block";
}

// Obtener la URL actual
const currentUrl = window.location.href;

// Verificar si la URL actual corresponde a http://127.0.0.1:5001/upload
if (currentUrl === "http://127.0.0.1:5001/upload") {
  // Construir la URL de redirección
  const redirectUrl = "http://127.0.0.1:5001/upload#ingresos-container";

  // Redirigir automáticamente a la URL de redirección
  window.location.replace(redirectUrl);
}
