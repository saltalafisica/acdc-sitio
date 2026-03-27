# Donde van las cosas

El carrusel que esta en la primer pagina esta en la carpeta `data/carousel/*.yaml`.

La imagen de fondo del carrusel es la imagen `static/img/photogrid.png`.

Los logos `public/img/logo`.

## Scripts utiles

### Agarra todas las imagenes en una carpeta y les da un tamaño de maximo 1200px y las optimiza para la web. se puede hacer mas ojo

```bash
magick mogrify -path output -resize 1200x\> -strip -interlace Plane -quality 82 *.jpeg
```
