package org.velezreyes.quiz.question6;

public class KarenTea implements Drink{
    public String name;
    public boolean isfizzy;
    public KarenTea(){
        this.name = "KarenTea";
        this.isfizzy = false;
    }
    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public boolean isFizzy() {
        return this.isfizzy;
    }
    
}
