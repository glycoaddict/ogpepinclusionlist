import numpy as np
import pandas as pd
import re
import os

H = 1.007276

class ogpeps:
    def __init__(self, charge_list=[1]):
        self.charge_list = charge_list
        f = r'C:\Users\choom.000\Google Drive\Postdoc\045 Calnexin Bard\Masses of sCANX O-glycopeptides SHORTLIST.xlsx'
        self.df = pd.read_excel(f, skiprows=[1])

        self.clean_peptides()
        self.get_flattened_pep_list()




    def clean_peptides(self):
        self.df['PEP'] = self.df['PEP'].apply(lambda x : (re.sub(r'\(.*', '', x)))
        mask = self.df['PEP'].apply(lambda x : True if ('T' in x) or ('S' in x) else False)
        self.df = self.df.loc[mask,:]



    def get_flattened_pep_list(self):
        # first get the charge states
        charged_pep_list = np.array([])
        ground_state_df = self.df.iloc[:, 1:].set_index('PEP')


        for z in self.charge_list:
            charged_values = (ground_state_df + H*z)/z

            # format it into a df
            charged_values = charged_values.apply(lambda x: x.apply(lambda y, t: (round(y, 4), t), args=(z,)), axis=1)
            charged_values = charged_values.to_numpy().flatten()

            # append the list
            charged_pep_list = np.append(charged_pep_list, charged_values)


        # split into dataframe
        res_df = pd.DataFrame(charged_pep_list)
        result_df = pd.DataFrame()
        result_df['m/z'] = res_df.iloc[:,0].apply(lambda x: x[0])
        result_df['z'] = res_df.iloc[:,0].apply(lambda x: x[1])
        result_df = result_df.loc[result_df.iloc[:, 0].between(300, 2000)].sort_values('m/z', axis=0)


        self.hit_list_df = result_df
        # self.hit_list_df = self.hit_list_df.loc[self.hit_list_df.iloc[:, 0].between(300, 2000)]

        return result_df


    def export_hitlist(self, file_name):
        writer = pd.ExcelWriter(os.path.splitext(file_name)[0]+'.xlsx')
        self.hit_list_df.to_excel(writer, index=False)
        writer.save()
        self.hit_list_df.to_csv(os.path.splitext(file_name)[0]+'.csv', index=False)


if __name__ == '__main__':
    o = ogpeps(charge_list=[2,3,4,5])
    o.export_hitlist(file_name='scanx SHORT ogpep hitlist for fusion')