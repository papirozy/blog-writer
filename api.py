import os
from flask import Flask, request, jsonify
from backend.generate_blog import generate_blog


# initialize the flask app
app = Flask(__name__)

# create a route
@app.route('/generate', methods = ['POST'])
def generate_blog_route():
    # take input from user
    data = request.json
    # it will save it to topic
    topic = data.get("topic", "")

    # if no topic is supplied, raise an error
    if not topic:
        return jsonify({'error': 'Topic is required'}), 400
    
    # if a topic is entered, call the generate function
    blog = generate_blog(topic)

    # save the generated blog into a file
    blog_filename = f"blogs/{topic.replace(' ','_').lower()}.md"
    with open(blog_filename, 'w', encoding = 'utf-8') as f:
        f.write(blog)
    
    return jsonify({'message':'Blog generated successfully!', 'blog' : blog})



if __name__ == "__main__":
    os.makedirs('blogs', exist_ok = True)
    app.run(debug = True)

    