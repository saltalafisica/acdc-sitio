# Donde van las cosas

El carrusel que esta en la primer pagina esta en la carpeta `data/carousel/*.yaml`.

La imagen de fondo del carrusel es la imagen `static/img/photogrid.png`.

Los logos `public/img/logo`.

## Scripts utiles

### Agarra todas las imagenes en una carpeta y les da un tamaño de maximo 1200px y las optimiza para la web. se puede hacer mas ojo

```bash
magick mogrify -path output -resize 1200x\> -strip -interlace Plane -quality 82 *.jpeg
```

## TODO

- [x] Fix upper case troughot all of the text
- [ ] Get the new favicon
- [ ] Ensure the banner image is displayed correctly
- [ ] Make giant tables scrollable
- [ ] Fix translation issues in the table of contents (i38)
- [ ] Make the tag column togglable
- [ ] Increase the width of the content column
- [ ] Display all affiliations
- [ ] Optimize images for the website
- [ ] Meta open graph optimization
- [ ] SEO optimization
- [ ] Setting the domain name
- [ ] Document how to add a post and modify the site
- [ ] RSS feed
- [ ] Other contribution channels
