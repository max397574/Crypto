#rot13 decoder
import codecs
text_rot13='rapbqr'
text= codecs.decode(text_rot13, 'rot_13')
print(text)
