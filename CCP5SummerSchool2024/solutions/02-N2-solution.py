# We can extract and display the full set of eigenvalues in a table, remembering to convert to eV
eigs = []
for log in [LDA, HF, PBE0]:
    eigs.append([27.211 * e for e in log.evals[0].tolist()[0]])
    
import pandas as pd
table = pd.DataFrame(eigs, index=['LDA', 'HF', 'PBE0'])
table

# The results differ from those in the table, since we a) used a pseudopotential, and b) didn't pay any attention to converging the basis set