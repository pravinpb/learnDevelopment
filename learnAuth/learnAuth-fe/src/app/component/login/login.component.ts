import { Component,OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';




@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent{
  message = '';
  loginForm = new FormGroup({
    usernanme: new FormControl('', Validators.required),
    password: new FormControl('', Validators.required)
  }); // Add closing parenthesis here
constructor() { }
}
