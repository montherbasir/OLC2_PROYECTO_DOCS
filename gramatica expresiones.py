def p_stmtList(t) :
  '''
  stmtList : stmtList stmt
                | stmt
  '''

def p_stmt(t) :
  '''
  stmt : selectStmt S_PUNTOCOMA
        | createStmt S_PUNTOCOMA
        | showStmt S_PUNTOCOMA
        | alterStmt S_PUNTOCOMA
        | dropStmt S_PUNTOCOMA
        | insertStmt S_PUNTOCOMA
        | updateStmt S_PUNTOCOMA
        | deleteStmt S_PUNTOCOMA
        | truncateStmt S_PUNTOCOMA
        | useStmt S_PUNTOCOMA
  '''

def p_expresion(t) :
  '''
  expresion : datatype
            | expComp
            | expBool
            | S_PARIZQ selectStmt S_PARDER
  '''

def p_funcCall(t) :
  '''
  funcCall : funcMath S_PARIZQ paramList S_PARDER
            | funcBool S_PARIZQ paramList S_PARDER
            | funcTrig S_PARIZQ paramList S_PARDER
  '''

def p_extract(t) :
  '''
  extract : R_EXTRACT S_PARIZQ optsExtract R_FROM timeStamp S_PARDER
  '''

def p_timeStamp(t) :
  '''
  timeStamp : R_TIMESTAMP stringLit
        | R_INTERVAL stringLit
  '''

def p_optsExtract(t) :
  '''
  optsExtract : R_YEAR
                | R_MONTH
                | R_DAY
                | R_HOUR 
                | R_MINUTE
                | R_SECOND
  '''

def p_datePart(t) :
  '''
  datePart : DATE_PART S_PARIZQ stringLit S_COMA dateSource S_PARDER
  '''

def p_dateSource(t) :
  '''
  dateSource : R_TIMESTAMP stringLit
        | R_DATE stringLit
        | R_TIME stringLit
        | R_INTERVAL intervalFields stringLit
        | R_NOW S_PARIZQ S_PARDER
  '''

def p_current(t) :
  '''
  current : CURRENT_DATE
        | CURRENT_TIME
        | timeStamp
  '''

def p_expComp(t) :
  '''
  expComp : datatype OL_MENORQUE datatype
            | datatype OL_MAYORQUE datatype
            | datatype OL_MAYORIGUALQUE datatype
            | datatype OL_MENORIGUALQUE datatype
            | datatype OL_ESIGUAL datatype
            | datatype 'OL_DISTINTODE' datatype
            | datatype 'OL_DISTINTODE' datatype
            | datatype R_BETWEEN datatype R_AND datatype
            | datatype R_NOT R_BETWEEN datatype R_AND datatype
            | datatype R_BETWEEN R_SYMMETRIC datatype R_AND datatype
            | datatype R_IS R_DISTINCT R_FROM datatype
            | datatype R_IS R_NOT R_DISTINCT R_FROM datatype
            | datatype R_IS R_NULL
            | datatype R_IS R_NOT R_NULL
            | datatype R_ISNULL
            | datatype R_NOTNULL
            | datatype R_IS R_TRUE
            | datatype R_IS R_NOT R_TRUE
            | datatype R_IS R_FALSE
            | datatype R_IS R_NOT R_FALSE
            | datatype R_IS R_UNKNOWN
            | datatype R_IS R_NOT R_UNKNOWN
  '''

def p_expSubq(t) :
  '''
  expSubq : datatype OL_MENORQUE  subqValues S_PARIZQ selectStmt S_PARDER
            | datatype OL_MAYORQUE  subqValues S_PARIZQ selectStmt S_PARDER
            | datatype OL_MAYORIGUALQUE subqValues S_PARIZQ selectStmt S_PARDER
            | datatype OL_MENORIGUALQUE subqValues S_PARIZQ selectStmt S_PARDER
            | datatype OL_ESIGUAL  subqValues S_PARIZQ selectStmt S_PARDER
            | datatype 'OL_DISTINTODE' subqValues S_PARIZQ selectStmt S_PARDER
            | datatype 'OL_DISTINTODE' subqValues S_PARIZQ selectStmt S_PARDER
            | datatype R_BETWEEN datatype R_AND datatype subqValues S_PARIZQ selectStmt S_PARDER
            | datatype R_NOT R_BETWEEN datatype R_AND datatype subqValues S_PARIZQ selectStmt S_PARDER
            | datatype R_BETWEEN R_SYMMETRIC datatype R_AND datatype subqValues S_PARIZQ selectStmt S_PARDER
            | datatype R_IS R_DISTINCT R_FFROM datatype subqValues S_PARIZQ selectStmt S_PARDER
            | datatype R_IS R_NOT R_DISTINCT R_FROM datatype subqValues S_PARIZQ selectStmt S_PARDER
            | datatype R_IS R_NULL subqValues S_PARIZQ selectStmt S_PARDER
            | datatype R_IS R_NOT R_NULL subqValues S_PARIZQ selectStmt S_PARDER
            | datatype R_ISNULL subqValues S_PARIZQ selectStmt S_PARDER
            | datatype R_NOTNULL subqValues S_PARIZQ selectStmt S_PARDER
            | datatype R_IS R_TRUE subqValues S_PARIZQ selectStmt S_PARDER
            | datatype R_IS R_NOT R_TRUE subqValues S_PARIZQ selectStmt S_PARDER
            | datatype R_IS R_FALSE subqValues S_PARIZQ selectStmt S_PARDER
            | datatype R_IS R_NOT R_FALSE subqValues S_PARIZQ selectStmt S_PARDER
            | datatype R_IS R_UNKNOWN subqValues S_PARIZQ selectStmt S_PARDER
            | datatype R_IS R_NOT R_UNKNOWN subqValues S_PARIZQ selectStmt S_PARDER
            | stringExp R_LIKE pattern 
  '''

def p_stringExp(t) :
  '''
  stringExp : stringLit
        | colName
  '''

def p_subqValues(t) :
  '''
  subqValues : R_ALL
                | R_ANY
                | R_SOME
  '''

def p_boolean(t) :
  '''
  boolean : expComp
            | litBool
            | R_EXISTS S_PARIZQ selectStmt S_PARDER
            | datatype R_IN S_PARIZQ selectStmt S_PARDER
            | datatype R_NOT R_IN S_PARIZQ selectStmt S_PARDER
            | expSubq
  '''

def p_expBool(t) :
  '''
  expBool : expBool R_AND expBool
            | expBool R_OR expBool
            | R_NOT expBool
            | boolean
  '''

def p_booleanCheck(t) :
  '''
  booleanCheck : expComp
            | litBool
  '''

def p_expBoolCheck(t) :
  '''
  expBoolCheck : expBoolCheck R_AND expBoolCheck
            | expBoolCheck R_OR expBoolCheck
            | R_NOT expBoolCheck
            | booleanCheck
  '''

