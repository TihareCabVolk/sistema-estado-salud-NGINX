// Función para consultar el estado actual
async function cargarEstado() {
    try {
        const response = await fetch('/estado');
        const data = await response.json();
        
        document.getElementById('cupos-texto').innerText = data.cupos_restantes;
        document.getElementById('nodo-texto').innerText = 'Contenedor ' + data.atendido_por_contenedor + ' (Puerto ' + data.puerto_interno + ')';
        
        const card = document.getElementById('status-card');
        if (data.cupos_restantes > 0) {
            card.className = "bg-green-100 border-l-4 border-green-500 p-4 mb-6 transition-colors duration-300";
            card.querySelector('h2').className = "text-2xl font-bold text-green-700";
        } else {
            card.className = "bg-red-100 border-l-4 border-red-500 p-4 mb-6 transition-colors duration-300";
            card.querySelector('h2').className = "text-2xl font-bold text-red-700";
            document.getElementById('cupos-texto').innerText = "AGOTADO";
        }
    } catch (error) {
        console.error("Error conectando a la API", error);
    }
}

// Función para el botón de reserva (POST)
async function hacerReserva() {
    try {
        await fetch('/reserva', { method: 'POST' });
        cargarEstado(); // Recargamos los datos inmediatamente
    } catch (error) {
        alert("Error al intentar reservar");
    }
}

// Función para el botón de cancelar reserva (DELETE)
async function cancelarReserva() {
    try {
        const response = await fetch('/reserva', { method: 'DELETE' });
        
        // Verificamos si hubo un error (como intentar cancelar cuando ya hay 20 cupos)
        if (!response.ok) {
            const data = await response.json();
            alert(data.error); // Muestra el mensaje: "No hay reservas para cancelar..."
        }
        
        cargarEstado(); // Recargamos los datos inmediatamente para ver la suma
    } catch (error) {
        alert("Error al intentar cancelar la reserva");
    }
}

// Cargar datos al abrir la página y actualizar cada 2 segundos
cargarEstado();
setInterval(cargarEstado, 2000);