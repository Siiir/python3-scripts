import fitz, os
dir_path= r"G:\"
pdf_file= dir_path+ r"\scan0003.pdf"; save_to= dir_path;
with fitz.open(pdf_file) as doc:
    digits = len(str(doc.page_count))
    for i, page in enumerate(doc):
        if doc.page_count>1:
            page_id = f'{{:0{digits}}}'.format(i+1)
            file_name = f'{os.path.split(pdf_file)[1][:-4]}_p{page_id}.png'
        else:
            file_name = f'{os.path.split(pdf_file)[1][:-4]}.png'
        png_file = os.path.join(save_to, file_name)
        trans = fitz.Matrix(1.0, 1.0).prerotate(0) # zoom_x, zoom_y
        pm = page.get_pixmap(matrix=trans, alpha=False)
        pm.save(png_file)
        
        
        