from flask import *
import pandas as pd
app = Flask(__name__)

@app.route("/table")
def show_tables():
    # format metadata file
    metadata = pd.read_csv('../python-full-stack-API-example/sample_files/metadata (1).txt', sep='\t')

    # make a png table
    # png_names_np = metadata['imageNames'].values
    # png_names = pd.DataFrame(data= png_names_np)

    return render_template('view.html', tables=[metadata.to_html(classes='metadata')],
                           titles=['metadata'])


@app.route("/file-downloads") # this is a job for GET
def file_downloads():
    return send_file('../python-full-stack-API-example/sample_files/metadata (1).txt',
                     as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
