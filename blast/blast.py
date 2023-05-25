import re

class BlastParser:
    def __init__(self, file_path):
        self.file_path = file_path
        

    def parse(self):
        with open(self.file_path, "r") as file:
            content = file.read()

        results = re.split("<Iteration>\n", content)
        for result in results:
            match = re.search("<Iteration_query-def>(.+)</Iteration_query-def>", result)
            if match:
                query = match.group(1)
                hits = re.findall("<Hit>(.*?)</Hit>", result, re.DOTALL)
                for num, hit in enumerate(hits, start=1):
                    hit_id = re.search("<Hit_id>(\S+)</Hit_id>", hit).group(1)
                    hit_def = re.search("<Hit_def>(.*?)</Hit_def>", hit).group(1)

                    hsps = re.findall("<Hsp>(.*?)</Hsp>", hit, re.DOTALL)
                    for hsp in hsps:
                        query_from = re.search("<Hsp_query-from>(\S+)</Hsp_query-from>", hsp).group(1)
                        query_to = re.search("<Hsp_query-to>(\S+)</Hsp_query-to>", hsp).group(1)
                        hit_frame = re.search("<Hsp_query-frame>(\S+)</Hsp_query-frame>", hsp).group(1)
                        align_len = re.search("<Hsp_align-len>(\S+)</Hsp_align-len>", hsp).group(1)
                        self.print_result(query, num, align_len, hit_frame, query_from, query_to, hit_id, hit_def)

    def print_result(self, query, num, align_len, hit_frame, query_from, query_to, hit_id, hit_def):
        print(f">query_name:{query};num{num};len={align_len};frame:{hit_frame};query_start:{query_from};query_end:{query_to};{hit_id};{hit_def}")\
        
    
        
    @property
    def db(self):
            with open(self.file_path, "r") as file:
                content = file.read()   
            db=re.search("<BlastOutput_db>(.+)</BlastOutput_db>", content).group(1)
            print(db)
            
    def parse_para(self):
        with open(self.file_path, "r") as file:
                content = file.read()
        expect=re.search("<Parameters_expect>(.+)</Parameters_expect>", content).group(1)
        match=re.search("<Parameters_sc-match>(.+)</Parameters_sc-match>", content).group(1)
        mismatch=re.search("<Parameters_sc-mismatch>(.+)</Parameters_sc-mismatch>", content).group(1)    
        filter1=re.search("<Parameters_filter>(.+)</Parameters_filter>", content).group(1)   
        self.print_para(expect,match,mismatch,filter1)
        
    def print_para(self,expect,match,mismatch,filter1):
        print(f"e_value:{expect};match_score:{match};mismatch_score:{mismatch};filter_method:{filter1}")
              
    @property        
    def version(self):
            with open(self.file_path, "r") as file:
                content = file.read()
            version=re.search("<BlastOutput_version>(.+)</BlastOutput_version>", content).group(1)
            print(version)
    
            
    def parse_hit(self):
        with open(self.file_path, "r") as file:
            content = file.read()
        results = re.split("<Iteration>\n", content)
        for result in results:
            match = re.search("<Iteration_query-def>(.+)</Iteration_query-def>", result)
            if match:
                hits = re.findall("<Hit>(.*?)</Hit>", result, re.DOTALL)
                for num_his, hit in enumerate(hits, start=1):
                    hit_id = re.search("<Hit_id>(\S+)</Hit_id>", hit).group(1)
                    hit_def = re.search("<Hit_def>(.*?)</Hit_def>", hit).group(1)
                    hit_accession=re.search("<Hit_accession>(.*?)</Hit_accession>", hit).group(1)
                    hsps = re.findall("<Hsp>(.*?)</Hsp>", hit, re.DOTALL)
                    for num_hsp, hsp in enumerate(hsps, start=1):
                        hsp_bitscore=re.search("<Hsp_bit-score>(.*?)</Hsp_bit-score>", hsp).group(1)
                        hsp_score=re.search("<Hsp_score>(.*?)</Hsp_score>", hsp).group(1)
                        hsp_evalue=re.search("<Hsp_evalue>(.*?)</Hsp_evalue>", hsp).group(1)
                        self.print_hit(num_his,hit_id,hit_def,hit_accession,num_hsp,hsp_bitscore,hsp_score,hsp_evalue)

    def print_hit(self,num_his,hit_id,hit_def,hit_accession,num_hsp,hsp_bitscore,hsp_score,hsp_evalue):
        print(f">his_num:{num_his};hit_id:{hit_id};hit:{hit_def};accession:{hit_accession}\n>>hsp_num:{num_hsp};bitscore:{hsp_bitscore};score:{hsp_score};evalue:{hsp_evalue}")


    def parse_seq(self):
        with open(self.file_path, "r") as file:
            content = file.read() 
        results = re.split("<Iteration>\n", content)
        for result in results:
            match = re.search("<Iteration_query-def>(.+)</Iteration_query-def>", result)
            if match:
                hits = re.findall("<Hit>(.*?)</Hit>", result, re.DOTALL)
                for num_his, hit in enumerate(hits, start=1):
                    hsps = re.findall("<Hsp>(.*?)</Hsp>", hit, re.DOTALL)
                    for num_hsp, hsp in enumerate(hsps, start=1):
                        query_start=re.search("<Hsp_query-from>(\S+)</Hsp_query-from>", hsp).group(1)
                        query_end=re.search("<Hsp_query-to>(\S+)</Hsp_query-to>", hsp).group(1)
                        hit_start=re.search("<Hsp_hit-from>(\S+)</Hsp_hit-from>", hsp).group(1)
                        hit_end=re.search("<Hsp_hit-to>(\S+)</Hsp_hit-to>", hsp).group(1)
                        query_seq=re.search("<Hsp_qseq>(\S+)</Hsp_qseq>", hsp).group(1)
                        hit_seq=re.search("<Hsp_hseq>(\S+)</Hsp_hseq>", hsp).group(1)
                        midline=re.search("<Hsp_midline>(.+)</Hsp_midline>", hsp).group(1)
                        self.print_seq(num_his,num_hsp,query_start,query_end,hit_start,hit_end,query_seq,hit_seq,midline)

    def print_seq(self,num_his,num_hsp,q_start,q_end,h_start,h_end,query,hit,midline):
        print(f">his_num:{num_his};hsp_num:{num_hsp}\nquery_start:{q_start};query_end:{q_end}\n{query}\n{midline}\n{hit}\nhit_start:{h_start};hit_end:{h_end}")

    @property
    def hit_seq(self):
        with open(self.file_path, "r") as file:
            content = file.read() 
        results = re.split("<Iteration>\n", content)
        for result in results:
            match = re.search("<Iteration_query-def>(.+)</Iteration_query-def>", result)
            if match:
                hits = re.findall("<Hit>(.*?)</Hit>", result, re.DOTALL)
                for num_his, hit in enumerate(hits, start=1):
                    hsps = re.findall("<Hsp>(.*?)</Hsp>", hit, re.DOTALL)
                    for num_hsp, hsp in enumerate(hsps, start=1):
                        hit_seq=re.search("<Hsp_hseq>(\S+)</Hsp_hseq>", hsp).group(1)
                        self.print_hitseq(num_his,num_hsp,hit_seq)
                        
    def print_hitseq(self,num_his,num_hsp,hit_seq):
        print(f">his_num:{num_his};hsp_num:{num_hsp}\n{hit_seq}")
                        
                        
