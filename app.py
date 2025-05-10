import streamlit as st

st.titl("HELLO, WELCOME TO THIS APP")


st.text("HI")

 #include <stdio.h>                                                                                       

int main()
{
    int c,l,e,a;scanf("%d %d %d %d",&c,&l,&e,&a);
    int pay=0;
    int promo;
    
    if(c>0){
        pay=c*50;
        promo=pay-(c*5);
    if (pay<100){pay + 25;}
    }
    
    if(l>0){
        pay=l*45;
        promo=pay-(l*5);
    if (pay<100){pay + 25;}
    }
    
    if(e>0){
        pay=e*40;
        promo=pay-(e*5);
    if (pay<100){pay + 25;}
    }
    
    if(a>0){
        pay=a*35;
        promo=pay-(a*5);
    if (pay<100){pay + 25;}
    }
    
    
    printf("%d baht",pay);
    

    return 0;
}
