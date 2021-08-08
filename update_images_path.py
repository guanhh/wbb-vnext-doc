
import os
import re

#要改的文件夹
dir ="D:\\File\\Test\\github\\wbb_doc_site"

#要改的文件类型（可以输入多个）
file_type=[".html"]

#替换表（可以用python正则表达式）
look_up_table=[
               ["https://github.com/guanhh/wbb-vnext-doc/blob/main/","https://raw.githubusercontent.com/guanhh/wbb-vnext-doc/main/"],
               ]

def get_filelist(dir,filetype):
    Filelist = []
    for home, dirs, files in os.walk(dir):
        for filename in files:
            if(filename[-len(filetype):]==filetype):
                Filelist.append(os.path.join(home, filename))
    return Filelist

if __name__ =="__main__":
    for type in file_type:
        print("开始处理"+type+"类型文件")
        file_list = get_filelist(dir,type)
        print("共发现"+str(len(file_list))+"个"+type+"类型文件")
        replace_count=0
        file_count=0
        for file in  file_list:
            file_count=file_count+1
            if(file_count%100==0):
                print("修改到第"+str(file_count)+"个文件")
            file_data=""
            with open(file, "r", encoding="ISO-8859-1") as f:
                for line in f:
                    for item in look_up_table:
                        if re.search(item[0], line):
                            #print("正在修改从"+item[0]+"到"+item[1])
                            line=re.sub(item[0],item[1],line)
                            replace_count=replace_count+1
                    file_data += line
            with open(file,"w",encoding="ISO-8859-1") as f:
                f.write(file_data)
        print("一共进行了"+str(replace_count)+"处替换")
        print("结束处理"+type+"类型文件")
print("全部结束")

