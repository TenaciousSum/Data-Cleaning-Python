import pandas as pd

# ====================================================================================================
# ================================ Series type --> dtype: object =====================================
# ====================================================================================================

s = pd.Series(['Python is love!', 'R is good as well.', 'Tableu helps to visualize data with good insights.'])
print(s)

# ====================================================================================================
# ================================ Series type --> dtype: string =====================================
# ====================================================================================================

s1 = pd.Series(['Python is love!', 'R is good as well.', 'Tableu helps to visualize data with good insights.'],
                dtype = "string")
print(s1)

# ====================================================================================================
# ======================= counting the umber of string --> count() method ============================
# ====================================================================================================

print(s1.str.count('Python'))

# ====================================================================================================
# ========================================  isdigit() method =========================================
# ====================================================================================================

s2 = pd.Series(['102', 'Pandas', '22', '242', 'Pandas', '102'], dtype="string")
print(s2.str.isdigit())

# ====================================================================================================
# ======================= finding any match in the string --> match() method =========================
# ====================================================================================================

print(s2.str.match('102'))
print(s2.str.match('Pan'))

# ====================================================================================================
# ===========================  capitalize each text --> upper() method ===============================
# ====================================================================================================

s1 = pd.Series(['Python is love!', 'R is good as well.', 'Tableu helps to visualize data with good insights.'],
                dtype="string")
s_upper = s1.str.upper()
print(s_upper)

# ====================================================================================================
# ===========================  lower case each text --> upper() method ===============================
# ====================================================================================================

s_lower = s_upper.str.lower()
print(s_lower)

# ====================================================================================================
# ===========================  length of each string --> len() method ================================
# ====================================================================================================

print(s1.str.len())

# ====================================================================================================
# ============================  remove whitespace --> strip() method =================================
# ====================================================================================================

s3 = pd.Series([' Python', 'R', 'Ruby ', 'Fortran '])
print(s3)

#0      Python
#1           R
#2       Ruby
#3    Fortran 
#dtype: object

print(s3.str.strip())

# ====================================================================================================
# ==========================  remove left whitespace --> lstrip() method =============================
# ====================================================================================================

print(s3.str.lstrip())

# ====================================================================================================
# ==========================  remove right whitespace --> rstrip() method ============================
# ====================================================================================================

print(s3.str.rstrip())

# ====================================================================================================
# ==========================  cleaning '\n' and ' \n' --> strip() method =============================
# ====================================================================================================

s4 = pd.Series([' Python\n', 'R\n', 'Ruby \n', 'Fortran \n'], dtype='string')
print(s4)

#0      Python
#1           R
#2       Ruby
#3    Fortran
#dtype: string

print(s4.str.strip('\n'))
print(s4.str.strip(' \n'))


# ====================================================================================================
# ==========================  more string cleaning --> replace() method ==============================
# ====================================================================================================

s5 = pd.Series(['$#5000', 'dollar5,000', 'dollar55000', '$500'], dtype="string")
print(s5)

#0         $#1200
#1    dollar1,000
#2    dollar10000
#3           $500
#dtype: string

s5 = s5.str.replace('#', '')
s5 = s5.str.replace('dollar', '$')
s5 = s5.str.replace(',', '')
print(s5)
