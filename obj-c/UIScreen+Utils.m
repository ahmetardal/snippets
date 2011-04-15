//
//  UIScreen+Utils.m
//  LiveGO
//
//  Created by Ahmet Ardal on 2/3/11.
//  Copyright 2011 Ahmet Ardal. All rights reserved.
//

#import "UIScreen+Utils.h"


@implementation UIScreen(Utils)

- (BOOL) isRetina
{
    return [self respondsToSelector:@selector(scale)] && ([self scale] == 2.0f);
}

@end
