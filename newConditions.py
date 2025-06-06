from __future__ import annotations
import sympy as sp
import salesStrategy as st

class NewConditions:
    table={
        '3.1':[lambda p1,p2:(-p1+p2+1)/2,'off','off'],
        '3.2':[lambda p1,p2:(1-((p1-p2+2)**2)/8),'off','off'],
        '3.3':[lambda p1,p2:((p1-p2+2)**2)/8,'off','on'],
        '3.4':[lambda p1,p2:(-4*p1+4*p2+3)/8,'off','hy'],
        '3.5':[lambda p1,p2:(-p1+p2+3)*(-p1+p2+1)/8,'off','hy'],
        '3.6':[lambda p1,p2:(1-((p1-p2+2)**2)/8),'on','off'],
        '3.7':[lambda p1,p2:((p1-p2+2)**2)/8,'on','off'],
        '3.8':[lambda p1,p2:(-p1+p2+1)/2,'on','on'],
        '3.9':[lambda p1,p2:(-4*p1+4*p2+3)/8,'on','hy'],
        '3.10':[lambda p1,p2:(-p1+p2+3)*(-p1+p2+1)/8, 'on','hy'],
        '3.11':[lambda p1,p2:1-((p1-p2+3)*(p1-p2+1)/8), 'hy','off'],
        '3.12':[lambda p1,p2:(-4*p1+4*p2+5)/8, 'hy', 'off'],
        '3.13':[lambda p1,p2:(p1-p2+3)*(p1-p2+1)/8, 'hy','on'],
        '3.14':[lambda p1,p2:(-4*p1+4*p2+5)/8, 'hy','on'],
        '3.15':[lambda p1,p2:(-p1+p2+1)/2,'hy','hy']
    }

