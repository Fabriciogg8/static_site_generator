# Static Site Generator

This project is a simple static site generator that converts Markdown files into HTML, allowing you to create a static website with ease.

## Features

- **Markdown to HTML Conversion**: Automatically converts all Markdown files in the `content` directory into HTML pages.
- **Template-Based Design**: Uses a customizable `template.html` file to maintain a consistent layout across all pages.
- **Static Assets Handling**: Copies all files from the `static` directory to the `public` directory, preserving the directory structure.
- **Local Development Server**: Includes a simple HTTP server to preview the generated site locally.

## Prerequisites

- **Python 3**: Ensure that Python 3 is installed on your system.

## Installation

1. **Clone the Repository**:

 ```bash
   git clone https://github.com/Fabriciogg8/static_site_generator.git
 ```

2. **Navigate to the Project Directory:**
 ```bash
    cd static_site_generator
 ```
## Usage

1. Add Your Content:

Place your Markdown (.md) files inside the content directory. The generator processes files recursively, so you can organize content into subdirectories as needed.

2. Add Static Assets:

Place any static assets (e.g., images, CSS files) in the static directory. These files will be copied to the public directory, maintaining the same structure.

3. Customize the Template:

Modify the template.html file to change the overall layout and design of your site. This template wraps around the content of each converted Markdown file.

4. Generate the Site:

Run the following command to generate the HTML files and start the local development server:
 ```bash
    sh main.sh
 ```
The generated site will be available at http://localhost:8888.

## Directory Structure

```php
static_site_generator/
├── content/          # Markdown files to be converted
├── public/           # Generated HTML files and copied static assets
├── src/              # Source code for the generator
├── static/           # Static assets to be included in the site
├── template.html     # HTML template for page layout
├── main.sh           # Script to build the site and start the server
└── test.sh           # Script to run tests (if applicable)
```

## Customization

* **Template Modification:** Edit the template.html file to change the header, footer, or overall layout. The content from each Markdown file will be injected into this template.
* **Styling:** Add custom CSS files to the static directory and link them in the template.html to apply custom styles to your site.

## Running Tests

If there are tests included in the test.sh script, you can execute them using:

 ```bash
    sh test.sh
 ```

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.