package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine{

  public int total = 0;

  public static VendingMachine getInstance() { 
    // Fix me!
    return new VendingMachineImpl();
  }

  @Override
  public void insertQuarter() {
    this.total = this.total + 25;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    if(name == "ScottCola"){
      if( this.total == 75){
        return new ScottCola();
      }
      else{
        throw new NotEnoughMoneyException();
      }
    }
    else if(name=="KarenTea"){
      if(this.total >= 100){
        return new KarenTea();
      }
      else{
        throw new NotEnoughMoneyException();
      }
    }
    else{
      throw new UnknownDrinkException();
    }
  }
}
