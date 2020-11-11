import sys

drugmappingfile = "/opt/drugcell/drug_data/compound_names.txt" 


def main():
	# load mapping between smiles and drug names
	smiles2name = {}
	with open(drugmappingfile, 'r') as fi:
		fi.readline()
		for line in fi:
			tokens = line.strip().split('\t')
			smiles2name[tokens[1]] = tokens[2]

	# read output of DrugCell and add drug name
	inputfile = sys.argv[1]
	outputfile = inputfile[:inputfile.rfind('.')] + '_mapped.txt'
	with open(inputfile, 'r') as fi, open(outputfile, 'w') as fo:
		fo.write("%s\t%s\t%s\t%s\n" % ('cell', 'drug_name', 'predicted_AUC', 'drug_smiles'))
		for line in fi:
			tokens = line.strip().split('\t')
		
			drugname = "unknown" 
			try:
				drugname = smiles2name[tokens[1]]
			except:
				pass

			fo.write("%s\t%s\t%s\t%s\n" % (tokens[0], drugname, tokens[3], tokens[1]))
		

if __name__ == "__main__":
	main()
