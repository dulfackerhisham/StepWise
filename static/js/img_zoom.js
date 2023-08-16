function imageZoom(imgID){
    let img = document.getElementById(imgID)
    let lens = document.getElementById('lens')

    lens.style.backgroundImage = 'url( ${img.src} )'

    let ratio = 3

    lens.style.backgroundSize = (img.width * ratio) + 'px ' + (img.height * ratio) + 'px '

}

imageZoom('featured-img')