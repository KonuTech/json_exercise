from pywebcopy import save_webpage

url = "https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html"
download_folder = ""

kwargs = {'bypass_robots': True, 'project_name': 'recognisable-name'}

save_webpage(url, download_folder, **kwargs)
