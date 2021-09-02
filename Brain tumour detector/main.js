let  predict = document.querySelector('.check')
let imageupload = document.querySelector('.none')

document.querySelector('input[type="file"]').addEventListener('change', function() {
    if (this.files && this.files[0]) {
        // var img = document.querySelector('.main .modal img');
        // img.onload = () => {
        //     URL.revokeObjectURL(img.src);  // no longer needed, free memory
        // }
        console.log(this.files[0])

        // img.src = URL.createObjectURL(this.files[0]); // set src to blob url
    }
});
function displayImageupload(e){
   if(imageupload.classList.contains('none'))
   {
       imageupload.classList.remove('none')
       imageupload.classList.add('modal')
   }
   else{
    imageupload.classList.remove('modal')
    imageupload.classList.add('none')

       
   }

}



predict.addEventListener('click',displayImageupload)
