function confirmacionEliminacion(id){
    Swal.fire({
        title: '¿Estas seguro?',
        text: "¡No podras deshacer esta acción!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: '¡Si, eliminar!',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
              window.location.href ="/faq-eliminar/"+id+"/"
          )
        }
      })
}

function Salida(){
  window.location.href ="/adminfaq/"
}