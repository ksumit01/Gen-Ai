import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CounterComponent } from './counter.component';

describe('CounterComponent', () => {
  let component: CounterComponent;
  let fixture: ComponentFixture<CounterComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CounterComponent],
    });
    fixture = TestBed.createComponent(CounterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
  it('should decrement count by 1', () => {
    component.count = 5;
    component.decreaseCount();
    expect(component.count).toBe(4);
  });

  it('should not decrement count below 0', () => {
    component.count = 0;
    component.decreaseCount();
    expect(component.count).toBe(0);
  });

  it('should reset count to 0', () => {
    component.count = 5;
    component.resetCount();
    expect(component.count).toBe(0);
  });
});
