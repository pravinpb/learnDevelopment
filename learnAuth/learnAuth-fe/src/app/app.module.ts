import { LoginComponent } from './component/login/login.component';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent
  ],
  imports: [
    BrowserModule,
    RouterModule,
    FormGroup,
    FormControl,
    Validators
  ],
  providers: [],
  bootstrap: [AppComponent]
})

export class AppModule { }