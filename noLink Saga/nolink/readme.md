## nolink
by gen3, easy (1/5)

## goal 
write a script that will auto click/follow the links, this can be client side in js or py requests.

## prompt
follow the trail link http://nolink.whatever:8080/

## solution
I'm not gonna write the code rn but you just get the current page then do a 
```python
req = request.get(earl)
## chop out <a href="/biggiehash">
newlink = base + req.text.search(r'<a href="(.*)">', string_one).group(1)
#goto 1 using newlink
```

## Flag
flag{8pLMNFOWbbORWq-tlNAu2f8r70pLPlBO}