import os
def make_dir(out_file):
    file_name=out_file.split('/')[-1]
    file_path=out_file.split('/')[0:-1]

    #test
    save_path='save_doc'

    rename_file='[DOC]'+file_name
    rename_file_path=os.path.join(save_path,rename_file)
    os.makedirs(save_path, exist_ok=True)
    return rename_file_path
def write_doc(out_file,lines):
    rename_file_path=make_dir(out_file)
    with open(rename_file_path, 'w', encoding='utf-8') as file:
        for line in lines:
                file.write(line)
                file.write('\n')
        file.close()
# if __name__ == '__main__':
#     out_file='test.txt'
#     lines=['1','2','3']
#     write_doc(out_file,lines)
    