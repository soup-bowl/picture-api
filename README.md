# 🖼️ Picture API

A completely vague name for a tool that responds with a random photo from a directory fed into it.

![](https://github.com/soup-bowl/picture-api/assets/11209477/f75efe8b-6d87-41cd-8f07-da8c89f71776)

Intending to be used with a **[Pico Inky Frame](https://shop.pimoroni.com/products/inky-frame-7-3)**.

> [!IMPORTANT]  
> I have replaced the API with a NodeRed powered solution instead. 

## Usage

```bash
docker run -p <port>:80 -v "/path/to/photos:/images:ro" ghcr.io/soup-bowl/picture-api:latest
```
or
```yml
version: '3'
services:
  picture-api:
    image: ghcr.io/soup-bowl/picture-api:latest
    ports:
      - "<port>:80"
    volumes:
      - "/path/to/photos:/images:ro"
```

In both, replace `<port>` and `/path/to/photos`.
