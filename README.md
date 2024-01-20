# Picture API

A completely vague name for a tool that responds with a random photo from a directory fed into it.

Usage

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
