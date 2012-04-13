#!/bin/env python
import os
import sys
import markdown

def process_title_and_layout(markdown_text):
    tmp = markdown_text.strip()
    title = ""
    layout = ""
    if(tmp.startswith("---\n")):
        start_index = markdown_text.find("---\n")
        end_index = markdown_text.find("---\n", start_index+4)
        if(end_index>-1):
            lines = markdown_text[start_index+4:end_index].split("\n")
            for line in lines:
                if(line.startswith("title:")):
                    title = line[6:].strip()
                elif(line.startswith("layout:")):
                    layout = line[7:].strip()
                    
        markdown_text = markdown_text[end_index+4:]
        
    return title, layout, markdown_text

dirList=os.listdir(sys.argv[1])
for fname in dirList:
    if(fname.endswith(".markdown")):
        
        input_file = fname
        output_file = os.path.splitext(input_file)[0] + ".html"

        f = open(input_file, 'r')
        mdtext = f.read().decode("utf-8")
        f.close()

        title, layout, mdtext = process_title_and_layout(mdtext)

        if(layout==""):
            layout="default"

        f = open('_layouts/'+layout+'.html', 'r')
        skeleton = f.read().decode("utf-8")
        f.close()
            
        content = markdown.markdown(mdtext, ['codehilite(css_class=codehilite,guess_lang=False)', 'footnotes', 'def_list', 'fenced_code'])

        skeleton = skeleton.replace("{{page.title}}", title)

        skeleton = skeleton.replace("{{content}}", content)


        out = open(output_file, 'w')
        out.write(skeleton.encode('utf-8'))
        out.close()

