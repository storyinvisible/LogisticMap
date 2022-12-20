"""
This file aims to work on the expansion of the logistic Map and take the most significant values
"""
from decimal import *
from copy import deepcopy
from random import randint
class Term:
    coeff =1
    r_power =1;
    x_power=1;
    def __init__(self,coeff,x ,r):
        getcontext().prec = 50
        self.coeff=coeff;
        self.r_power=r;
        self.x_power=x;
        self.with_r= True;
    def dx(self):
        return Term(self.coeff*self.x_power, self.x_power-1,self.r_power )
    def add(self, term):
        assert (term.x_power == self.x_power and term.r_power == self.r_power)
        new_coeff = term.coeff + self.coeff;
        return Term(new_coeff,self.x_power,self.r_power)
    def mul_terms(self,terms):
        terms_dict={}
        for i in range(len(terms)):
            terms[i] = self*terms[i]
    def pow2(self, terms):
        term1= deepcopy(terms)
        term2 = deepcopy(terms)
        terms_dict={} # to store the power of the x
        for i in term1:
            for j in term2:
                term = i*j
                if term.get_pow_str() not in terms_dict:
                    terms_dict[term.get_pow_str()]=term
                else:
                    terms_dict[term.get_pow_str()]= terms_dict[term.get_pow_str()]+term


        return list(terms_dict.values())
    def f_pow(self, terms):
        power = self.x_power
        initial_term= deepcopy(terms)
        terms_dict={}
        while power !=1:
            for term_a in terms:
                for term_b in initial_term:
                    term = term_a*term_b
                    if term.get_pow_str() not in terms_dict:
                        terms_dict[term.get_pow_str()]= term
                    else:
                        terms_dict[term.get_pow_str()]= terms_dict[term.get_pow_str()]+term
            initial_term= list(terms_dict.values())
            power-=1



        return initial_term

    def f(self,terms):
        terms = self.f_pow(terms)
        for i in range(len(terms)):
            terms[i].r_power+=self.r_power;
            terms[i].coeff*=self.coeff
        return terms

        return terms
    def value(self,x,r=None):
        if not self.with_r and r is None:
            x = Decimal(x)
            c = Decimal(self.coeff)
            return c *  (x ** self.x_power)
        x =Decimal(x)
        r = Decimal(r)
        c= Decimal(self.coeff)
        return c*(r**self.r_power)*(x**self.x_power)
    def r_value(self,r):
        self.coeff= self.coeff*(r**self.r_power)
        self.r_power=0
        self.with_r=False
    def dx(self):
        self.coeff = self.x_power
        self.x_power= self.x_power-1
    def dr(self):
        self.coeff= self.coeff*self.r_power;
        self.r_power=self.r_power-1
    def __add__(self, term):
        assert term.x_power==self.x_power and term.r_power==self.r_power
        return Term(term.coeff+self.coeff,self.x_power,self.r_power)
    def __mul__(self, terms):
        new_coeff= self.coeff*terms.coeff
        new_r_power=self.r_power+terms.r_power
        new_x_power=self.x_power+terms.x_power
        term = Term(new_coeff,new_x_power,new_r_power)
        return term
    def get_pow_str(self):
        if not self.with_r:
            return "x^{}".format(self.x_power)
        return"r^{}x^{}".format(self.r_power,self.x_power)

    def __str__(self):
        return "{}r^{}x^{}".format(self.coeff,self.r_power,self.x_power)
    def __eq__(self, terms):
        return (terms.x_power == self.x_power and terms.r_power == self.r_power)


def terms_sum(terms,x,r):
    final =0
    for term in terms:
        final+=term.value(x,r)
    return final
def logistic_map_sym(iters, terms):
    if iters==1:
        return terms
    else:
        term1a = Term(1, 1, 1)  # rx
        term2a = Term(-1, 2, 1)  # -rx^2
        term1=term1a.f(terms)
        term2= term2a.f(terms)
        terms= term1 +term2
        return logistic_map_sym(iters-1, terms)
term1 = Term(1, 1, 1)  # rx
term2 = Term(-1, 2, 1)  # -rx^2
#
def logistic_map(iters, r,x):
    if iters==1:
        return r*x*(1-x)
    else:
        xn= r*x*(1-x)
        return logistic_map(iters-1,r,xn)
idx =6
