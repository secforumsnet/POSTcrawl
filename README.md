
   <h1>Web Crawler for Forms with POST Method</h1>
    <p>This Python script is a web crawler designed to search for web pages that contain HTML forms using the POST method. It utilizes the <code>requests</code> library to send HTTP GET requests and <code>BeautifulSoup</code> for HTML parsing.</p>

   <h2>Usage</h2>
    <p>Before running the script, ensure you have the required libraries installed:</p>
    <pre><code>pip install requests beautifulsoup4</code></pre>

   <p>To run the script, follow these steps:</p>
    <ol>
        <li>Clone or download this repository.</li>
        <li>Open your terminal or command prompt.</li>
        <li>Navigate to the script's directory.</li>
        <li>Execute the script using Python:</li>
    </ol>

   <pre><code>python POSTcrawl.py</code></pre>

   <p>Follow the on-screen instructions to input the filename containing starting URLs. The script will then crawl the provided URLs and detect web pages with forms using the POST method, saving them in a file named <code>urls_with_post_forms.txt</code>.</p>

  <h2>Features</h2>
    <ul>
        <li>Crawls web pages to find forms using the POST method.</li>
        <li>Follows links to other pages and domains.</li>
        <li>Supports multiple starting URLs from an input file.</li>
    </ul>

  <h2>Example</h2>
    <p>Here's an example of how to structure your input file containing starting URLs:</p>

   <pre>
        <code>
https://example.com/page1
https://example.com/page2
https://example.com/page3
        </code>
    </pre>

  
