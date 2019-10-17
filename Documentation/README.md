
# Bot documentation
## Inline mode
  Inline bots: Users can interact with your bot via inline queries straight from the text input field in any chat. All they     need to do is start a message with your bot's username and then type a query.

```javascript  
  /command
```

# Controller documentation for the Bot

- /actor/{name}

Respuesta:
```javascript
{
  "name": "name",
  "info": "info",
  "movies": [...]
}
```
- /serie/{name}

Respuesta:
```javascript
{
  "name": "name",
  "info": "info",
  "rating": 5.0
}
```
- /movie/{name}

Respuesta:
```javascript
{
  "name": "name",
  "info": "info",
  "rating": 5.0
}
```
- /director/{name}

Respuesta:
```javascript
{
  "name": "name",
  "info": "info",
  "movies": [...]
}
```
- /trends/directors

Respuesta:
```javascript
{
  "directors":
    [ ["name": "name", "movies": [...]], ["name": "name", "movies": [...]],
      ["name": "name", "movies": [...]]]
}
```
- /trends/movies

Respuesta:
```javascript
{
  "movies":
    [ ["name": "name", "info": "info", "rating": 5.0], ["name": "name", "info": "info", "rating": 5.0],
      ["name": "name", "info": "info", "rating": 5.0]]
}
```
- /trends/series

Respuesta:
```javascript
{
  "series":
    [ ["name": "name", "info": "info", "rating": 5.0], ["name": "name", "info": "info", "rating": 5.0],
      ["name": "name", "info": "info", "rating": 5.0]]
}
```
- /rating/movie/{name}
- /rating/serie/{name}
- /rating/short/{name}

- /reception/movie/{name}
- /reception/serie/{name}
- /reception/short/{name}

  
