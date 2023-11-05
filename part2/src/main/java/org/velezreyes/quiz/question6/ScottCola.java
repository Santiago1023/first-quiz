package org.velezreyes.quiz.question6;

public class ScottCola implements Drink{
    public String name;
    public boolean isfizzy;
    public ScottCola(){
        this.name = "ScottCola";
        this.isfizzy = true;
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
