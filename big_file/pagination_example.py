import multiprocessing as mp
def proccess(line):
	l = line.split(',')
	info = {
		'jurisdiction_name': l[0],
		'count_participants': l[1],
		'count_female': l[2],
		'percent_female': l[3],
		'count_male': l[4],
		'percent_male': l[5],
		'count_gender_unknown': l[6],
		'percent_gender_unknown': l[7],
		'count_gender_total': l[8],
		'percent_gender_total': l[9],
		'count_pacific_islander': l[10],
		'percent_pacific_islander': l[11],
		'count_hispanic_latino': l[12],
		'percent_hispanic_latino': l[13],
		'count_american_indian': l[14],
		'percent_american_indian': l[15],
		'count_asian_non_hispanic': l[16],
		'percent_asian_non_hispanic': l[17],
		'count_white_non_hispanic': l[18],
		'percent_white_non_hispanic': l[19],
		'count_black_non_hispanic': l[20],
		'percent_black_non_hispanic': l[21],
		'count_other_ethnicity': l[22],
		'percent_other_etnicity': l[23],
		'count_ethnicity_unknown': l[24],
		'percent_ethnicity_unknown': l[25],
		'count_ethnicity_total': l[26],
		'percent_ethnicity_total': l[27],
		'count_permanent_resident_alien': l[28],
		'percent_permanent_resident_alien': l[29],
		'count_us_citizen': l[30],
		'percent_us_citizen': l[31],
		'count_other_citizen_status': l[32],
		'percent_other_citizen_status': l[33],
		'count_citizen_status_unknown': l[34],
		'percent_citizen_status_unknown': l[35],
		'count_citizen_status_total': l[36],
		'percent_citizen_status_total': l[37],
		'count_receives_public_assistance': l[38],
		'percent_receives_public_assistance': l[39],
		'count_nreceives_public_assistance': l[40],
		'percent_nreceives_public_assistance': l[41],
		'count_public_assistance_unknown': l[42],
		'percent_public_assistance_unknown': l[43],
		'count_public_assistance_total': l[44],
		'percent_public_assistance_total': l[45].replace('\n',''),
	}
	return info
def get_the_info( file ):
	with open(file) as f:
		data = f.readlines()
		for line in data:
			print( proccess( line ) )
def get_multi_info( file ):
	cores = 3
	pool = mp.Pool( cores )
	jobs = []

	with open(file) as f:
		data = f.readlines()
		for line in data:
			jobs.append( pool.apply_async(proccess, (line) ) )
	for job in jobs:
		print( job.get() )
	pool.close()
#get_the_info( "demografic.csv" )
get_multi_info( "demografic.csv" )