![travis-img](https://travis-ci.org/newslynx/lauteur.svg)
lauteur
======
_Tools for ascribing authorship - to the chagrin of [Barthes](http://en.wikipedia.org/wiki/Death_of_the_Author)_

**NOTE**: All functionality of this library has been improved upon and ported to [Newslynx V2](http://github.com/newslynx/newslynx), specifically [this module](https://github.com/newslynx/newslynx/blob/master/newslynx/lib/author.py).
## Install
```
pip install lauteur
```

## Test
Requires `nose`
```
nosetests
```

## Usage
`lauteur` has two methods: `from_string` and `from_html`

`from_string` is mostly used in RSS Feed parsing where authors are sometimes embedded as bylines:

```python
import lauteur

string = 'By: Brian Abelson ,and Michael H. Keller & Dr. Stijn Debrouwere IV'
authors = lauteur.from_string(string)
print authors

# ['Brian Abelson', 'Michael H Keller', 'DR Stijn Debrouwere IV']
```

`from_html` searches through common meta tags for authors.

```python
import lauteur
import requests

r = requests.get('http://www.nytimes.com/2013/12/20/books/michiko-kakutanis-10-favorite-books-of-2013.html')

authors = lauteur.from_html(r.content)
print authors
# ['Michiko Kakutani']
```

## Todo:

- [ ] Find more meta tags. 
- [ ] Improve name formatting algorithm.
