## DIRB: 
- a Web Content Scanner. It looks for existing (and/or hidden) Web Objects.
- It basically works by launching a dictionary basesd attack against a web server and analizing the response.

> Syntex: dirb <url_base> [<wordlist_file(s)>] [options]

## Example:
```
 dirb http://url/directory/ (Simple Test)
 dirb http://url/ -X .html (Test files with '.html' extension)
 dirb http://url/ /usr/share/dirb/wordlists/vulns/apache.txt (Test with apache.txt wordlist)
 dirb https://secure_url/ (Simple Test with SSL)
```

