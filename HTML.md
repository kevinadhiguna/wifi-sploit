## First, examples os html codes and their correct use for the `wfs-browser-input.py`:

index.html:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Test</title>
</head>
<body>
    <h1>Login</h1>
    <input type="text" id="username" placeholder="Username">
    <input type="password" id="password" placeholder="Password">
    <button id="button" onclick="checkLogin()">Login</button>
    <p id="message"></p>

    <script src="script.js"></script>
</body>
</html>
```

script.js:
```javascript
function checkLogin() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const message = document.getElementById('message');

    if (username === "admin" && password === "admin") {
        message.textContent = "Success";
    } else {
        message.textContent = "Invalid login";
    }
}
```

So, to begin with, we must identify the inputs and the html button:

```html 

<input type="text" id="username" placeholder="Username"> 
<input type="password" id=" password" placeholder="Password"> 
<button id="button" onclick="checkLogin()">Login</button> 
``` 

In this case, the correct use of `wfs-browser-input.py` would be like this: 

```bash
...
Username html element name (default: username): username 
Is username element an id or a name? (i/n): i 
Password html element name (default: password): password 
Is password element an id or a name? (i/n): i 
Button html element name (default: button): button 
Is button element an id or a name? (i/n): i
...
```

## Analyze error messages

According to the previous example, in the case of an incorrect login, the code will return the following sentence in the HTML: `Invalid login`
So for the python codes to identify the unsuccessful login, ensure that they have in the `expression` set the word `invalid` or whatever it is in your case.
