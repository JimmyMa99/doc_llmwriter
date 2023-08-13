import os
import argparse
from tqdm import tqdm

class CodeTomd_Processor:
    def __init__(self, args):
        self.args = args
        self.cpp_and_h_files = []

    def get_code_from_files(self, directory):
        cpp_and_h_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".cpp") or file.endswith(".h"):
                    cpp_and_h_files.append(os.path.join(root, file))
        self.cpp_and_h_files = cpp_and_h_files

    def remove_comments(self, source):
        ans = []
        t = []
        block_flag = False
        for s in source:
            i, m = 0, len(s)
            while i < m:
                if block_flag:
                    if i+1 < m and s[i:i+2] == "*/":
                        block_flag = False
                        i += 1
                else:
                    if i+1 < m and s[i:i+2] == "/*":
                        block_flag = True
                        i += 1
                    elif i+1 < m and s[i:i+2] == "//":
                        break
                    else:
                        t.append(s[i])
                i += 1
            if not block_flag and t:
                ans.append("".join(t))
                t.clear()
        return ans

    def read_line_save_md(self, file_path, save_path, code_list):
        spilt_file_name = file_path.split('/')[-1].split('.')[0] + '.md'
        to_file_name = os.path.join(save_path, spilt_file_name)
        with open(file_path, 'r') as file:
            for line in file:
                code_list.append(line)
            if self.args.removeComments:
                code_list = self.remove_comments(code_list)
            self.process_line_save_to_markdown(code_list, output_file=to_file_name)

    def process_line_save_to_markdown(self, lines, output_file):
        with open(output_file, 'a') as markdown_file:
            for line in lines:
                markdown_file.write(line)

    def process_files(self, file_path, save_path):
        code_list = []
        self.read_line_save_md(file_path, save_path, code_list)

    def main(self):
        self.get_code_from_files(self.args.code_dir)
        for file_path in tqdm(self.cpp_and_h_files):
            self.process_files(file_path, self.args.code_to_dir)

def get_arguments():
    parser = argparse.ArgumentParser(description='The code for get code.')
    parser.add_argument("--code_dir", type=str, default='/home/code/testcode')
    parser.add_argument("--code_to_dir", type=str, default='/home/code/testcode/to_dir_nocomment')
    parser.add_argument("--removeComments", type=bool, default=True)
    parser.add_argument("--prompt", type=str, default='')
    return parser

def deal_with_args(args):
    if not os.path.exists(args.code_dir):
        raise ValueError("code_dir does not exist")
    os.makedirs(args.code_to_dir, exist_ok=True)

def main():
    args = get_arguments().parse_args()
    deal_with_args(args)

    code_processor = CodeTomd_Processor(args)
    code_processor.main()

if __name__ == "__main__":
    main()
