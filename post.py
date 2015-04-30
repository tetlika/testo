from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc import WordPressPost

client = Client('http://localhost:8080/xmlrpc.php', 'admin', 'admin')

post = WordPressPost()

t = open('title.txt','r')
p = open('post.txt', 'r')

post.title = t.read()
post.content = p.read()
post.id = client.call(posts.NewPost(post))

#publish post
post.post_status = 'publish'
client.call(posts.EditPost(post.id, post))

t.close()
p.close()


