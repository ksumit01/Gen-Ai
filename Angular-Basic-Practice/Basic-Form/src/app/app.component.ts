import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'Basic-Form';
  userData: any = {};
  flag = true;
  color = 'red';
  getData(data: NgForm) {
    // console.log(data);
    this.userData = data.value;
    console.log(this.userData);
  }
  toggleElement() {
    this.flag = !this.flag;
    this.color = this.flag ? 'red' : 'green';
  }
}
