#!/usr/bin/env python
#encoding: utf-8


#################################################

links = open('links','r').readlines()
weaponList = ['AK-47',
			  #'AUG',
			  #'AWP',
			  #'CZ70-Auto',
			  'Desert%20Eagle',
			  'Dual%20Berettas',
			  #'FAMAS',
			  'Five-SeveN',
			  #'G3SG1',
			  #'Galil%20AR',
			  'Glock-18',
			  #'M249',
			  #'M4A1-S',
			  #'M4A4',
			  'MAC-10',
			  'MAG-7',
			  #'MP7',
			  #'MP9',
			  #'Negev',
			  #'Nova',
			  'P2000',
			  'P250',
			  'P90',
			  #'PP-Bizon',
			  #'R8%20Revolver',
			  #'Sawed-Off',
			  #'SCAR-20',
			  #'SG%20553',
			  #'SSG%2008',
			  'USP-S',
			  #'UMP-45',
			  'Tec-9',
			  #'XM1014',
			  ]


out = open('out_links','w')
for link in links:
	for w in weaponList:
		if w in link:
			out.write(link)
			break
out.close()