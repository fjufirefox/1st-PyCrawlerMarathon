import json, requests

resp_pop = requests.get(
    'https://www.dcard.tw/_api/forums/pet/posts?popular=true', params=None)

resp_npop = requests.get(
    'https://www.dcard.tw/_api/forums/pet/posts?popular=false', params=None)

resp_pop_datas = json.loads(resp_pop.text,
                            encoding=None,
                            cls=None,
                            object_hook=None,
                            parse_float=None,
                            parse_int=None,
                            parse_constant=None,
                            object_pairs_hook=None)

resp_npop_datas = json.loads(resp_npop.text,
                             encoding=None,
                             cls=None,
                             object_hook=None,
                             parse_float=None,
                             parse_int=None,
                             parse_constant=None,
                             object_pairs_hook=None)

# 1. 這個 API 一次會回傳幾筆資料？每一筆資料包含哪些欄位？
count_num = 0
for resp_pop_data in resp_pop_datas:
    count_num += 1

print('這個 API 一次會回傳%s筆資料？' % count_num)
print('每一筆資料包含哪些欄位？', resp_pop_datas[1].keys())
# 2. 取出每一筆資料的「標題」、「貼文時間」、「留言人數」、「按讚人數」
import pandas as pd

cols_name = ['標題', '貼文時間', '留言人數', '按讚人數']
df_pop_pd = pd.read_json(path_or_buf=resp_pop_datas.text,
                         orient=None,
                         typ="frame",
                         dtype=None,
                         convert_axes=None,
                         convert_dates=True,
                         keep_default_dates=True,
                         numpy=False,
                         precise_float=False,
                         date_unit=None,
                         encoding=None,
                         lines=False,
                         chunksize=None,
                         compression="infer")
df_npop_pd = pd.read_json(path_or_buf=resp_npop_datas.text,
                          orient=None,
                          typ="frame",
                          dtype=None,
                          convert_axes=None,
                          convert_dates=True,
                          keep_default_dates=True,
                          numpy=False,
                          precise_float=False,
                          date_unit=None,
                          encoding=None,
                          lines=False,
                          chunksize=None,
                          compression="infer")

df_pop_pd_r = df_pop_pd[['title'], ['createdAt'], ['commentCount'],
                        ['likeCount']]
df_pop_pd_r.columns = cols_name
df_pop_pd_r

df_npop_pd_r = df_npop_pd[['title'], ['createdAt'], ['commentCount'],
                          ['likeCount']]
df_npop_pd_r.columns = cols_name
df_npop_pd_r

# 3. 計算熱門/非熱門文章的「平均留言人數」與「平均按讚人數」
print('熱門文章的「平均留言人數」', df_npop_pd_r['留言人數'].mean())
print('熱門文章的「平均按讚人數」', df_npop_pd_r['按讚人數'].mean())
print('非熱門文章的「平均留言人數」', df_npop_pd_r['留言人數'].mean())
print('非熱門文章的「平均按讚人數」', df_npop_pd_r['按讚人數'].mean())
