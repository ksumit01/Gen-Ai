import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HelloComponent } from './hello/hello.component';
import { ModuleTestModule } from './module-test/module-test.module';
@NgModule({
  declarations: [AppComponent, HelloComponent],
  imports: [BrowserModule, AppRoutingModule, ModuleTestModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
