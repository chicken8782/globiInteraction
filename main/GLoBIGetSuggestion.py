#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pandas as pd
import numpy as np
import csv

#response = requests.get("http://api.globalbioticinteractions.org/interaction?sourceTaxon=Pieris&interactionType=eats")
#payload = response.json()

#df = pd.DataFrame(payload['data'], columns=payload['columns'])
#df_sep = df[['source_taxon_name', 'interaction_type' ,'target_taxon_name']]

ObservList = ["Brassica rapa pekinensis", "Brassica oleracea var. capitata", "Allium tuberosum", "Daucus carota subsp. sativus"]
pollinatorList = []

# 種名と相互作用タイプから関連種を取得する
def getSuggestion(spName, intType):
	url = ("http://api.globalbioticinteractions.org/interaction?sourceTaxon="+spName+"&interactionType="+intType)
	response = requests.get(url)
	df = pd.DataFrame(response.json()['data'], columns=response.json()['columns'])
	df_sep = df[['source_taxon_name', 'interaction_type' ,'target_taxon_name']]
	return df_sep

def callVegName():
	spList = ["ハクサイ","キャベツ","ニラ","ニンジン"]
	for i in spList:
		if i == "ハクサイ":
			print("ハクサイ！")
			continue
		print(i)

def suggest():
	#ObservList = ["Brassica rapa pekinensis", "Brassica oleracea var. capitata", "Allium tuberosum", "Daucus carota subsp. sativus"]
	for i in range(len(ObservList)):
		if i == 0:
			df_all = getSuggestion(ObservList[0],"interactsWith")
			continue
		else:
			df = getSuggestion(ObservList[i],"interactsWith") 
			df_all = df_all.append(df)


	df_all_count= df_all['target_taxon_name'].value_counts(normalize=True)

	#print("df_all_count\n")
	#print(df_all_count)

def globiApi(dataList, intType):
	#ObservList = ["Brassica rapa pekinensis", "Brassica oleracea var. capitata", "Allium tuberosum", "Daucus carota subsp. sativus"]
	for i in range(len(dataList)):
		if i == 0:
			df_all = getSuggestion(dataList[0],intType)
			continue
		else:
			df = getSuggestion(dataList[i],intType) 
			df_all = df_all.append(df)
	return (df_all)


def pollinatorList():
	
	#相互作用を取得

	#pollinatorList = globiApi("pollinatedBy")
	pollinatorList = globiApi(ObservList, "interactsWith")
	pollinatorList_count= pollinatorList['target_taxon_name'].value_counts(normalize=True)
	print(pollinatorList_count)
	
	#uniqueリストを出力する
	pollinatorList_unique = pollinatorList['target_taxon_name'].unique()
	print(pollinatorList_unique)
	pollinatorList.to_csv("180815pollinatorList.csv")
	pollinatorList_count.to_csv("180815pollinator_count.csv")
	
	#pollinatedされる種
	pollinatedList = globiApi(pollinatorList_unique, "pollinates")
	print(pollinatedList)	
	pollinatedList.to_csv("180815pollinatedList.csv")

	pollinatedList_count= pollinatedList['target_taxon_name'].value_counts(normalize=True)	
	pollinatedList_count.to_csv("180815pollinatedList_count.csv")
	#pollinatedList.to_csv(path_or_buf="/Users/outou1/Python/GLoBI/180815pollinatedList.csv", sep=', ', na_rep='', float_format=None, columns=None, header=True,index=True, index_label=None, mode='w', encoding=None, compression=None, quoting=None,
  

#List of interaction type : {"eats","eatenBy","pollinates","pollinatedBy","interactsWith","visitsFlowersOf"}
def main():

    #callVegName()
    #suggest()
    pollinatorList()

if __name__ == '__main__':
    main()

#====================================================

#csv_file = open("/Users/outou1/Python/GLoBI/YList20170621.csv", "r", encoding="ms932", errors="", newline="" )
#f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
#f = csv.reader(csv_file, delimiter=",")


#f_dict = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

#csv_input = pd.read_csv(filepath_or_buffer="/Users/outou1/Python/GLoBI/YList20170621.csv", encoding="ms932", sep=",")

#header = next(f)


#df2_uniq = df4['target_taxon_name'].unique()
#df_count= df['target_taxon_name'].value_counts()

#df4_count= df4['target_taxon_name'].value_counts()

#df_count= df['target_taxon_name'].value_counts(normalize=True)

#spList=["ハクサイ","キャベツ","ニラ","ニンジン"]
#for i in spList:
#	if i == "ハクサイ":
#		print("ハクサイ！")
#		continue
#	print(i)


#df.head()
