# Generated by Django 2.1.7 on 2019-03-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20190308_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='intro',
            field=models.TextField(default=' আশা করি হাতে কিছুটা সময় নিয়েই বসেছিস। এই জিনিসটা বানানোর ইচ্ছে সেই ক্লাস ১২ থেকে ছিল। এটা বানানোর একমাত্র উদ্দেশ্য হল ২০১৬ থেকে ২০১৯ পর্যন্ত সময়ের সবকটা ঘটনা/কান্ড যেন জমা করে রাখতে পারি এবং বহুবছর বাদে, কলেজে পড়ার সময় গুলোর কথা যখন মনে পড়বে, তখন তোদের এই সাইটে দেওয়া উত্তর গুলো পড়ে এই সময়ে ফিরে  আসতে  পারি। আমার সাথে ঘটে যাওয়া  সমস্ত ভালো/তিক্ত অভিজ্ঞতা যদি কিছু থেকে থাকে সেগুলো নির্দ্বিধায় এখানে বলে ফেলতে পারিস। \n\n* তোদের এই সমস্ত রেসপন্স আমি জুন মাসের আগে খুলে দেখব না। যাতে মনের কথা নির্দ্বিধায় লিখে ফেলতে পারিস।  \n* কোন ছবি দেওয়ার ইচ্ছে হলে google drive এ আপলোড করে এখানে link  দিয়ে দিতে পারিস।  '),
        ),
        migrations.AddField(
            model_name='customuser',
            name='out',
            field=models.TextField(default=' অনেক ধন্যবাদ। submit করার আগে একবার দেখে নে সব ঠিক আছে কিনা। জুন মাসের আগে যতবার খুশি তুই submit করতে পারবি। আর একটা অনুরোধ, যতক্ষণ না এই সাইটটার সম্পর্কে সবাই জানছে, এটা নিয়ে কারুর সাথে আলোচনা করিস না, নাহলে যারা এখন জানে না তাদের উৎসাহ টা আর একরকম থাকবে না।  '),
        ),
    ]